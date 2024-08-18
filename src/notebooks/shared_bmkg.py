import csv
import hashlib
import json
import os
import subprocess
import tarfile
import time

import gravis as gv
import igraph as ig
import pandas as pd
import requests
from tqdm.notebook import tqdm


# Web retrieval and validation


def check_internet_connection():
    urls = ["https://1.1.1.1", "https://8.8.8.8"]
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            continue
    return False


def ensure_internet_connection(retries=3, delay=10):
    for i in range(1, retries + 1):
        if check_internet_connection():
            break
        print(
            f"No internet connection. Retrying in {delay} seconds (Attempt {i} of {retries})."
        )
        time.sleep(delay)
    else:
        raise Exception(
            f"Failed to establish an internet connection after {retries} attempts."
        )


def get_remote_size(url):
    # Make sure there is an internet connection
    ensure_internet_connection()

    # Try to determine the size of the remote file
    try:
        # Attempt 1: HEAD request with "content-length" response attribute
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
        }
        response = requests.head(url, headers=headers, allow_redirects=True, timeout=10)
        remote_size = int(response.headers.get("content-length", 0))

        # Attempt 2: GET request with Range header and "content-range" response attribute
        if remote_size == 0:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
                "Range": "bytes=0-1",
            }
            response = requests.get(
                url, headers=headers, allow_redirects=True, timeout=10
            )
            content_range = response.headers.get("content-range")
            try:
                remote_size = int(content_range.split("/")[-1])
            except Exception:
                return 0
        return remote_size
    except requests.exceptions.RequestException as e:
        print(f"Error fetching remote size: {str(e)}")
        return 0


def get_local_size(filepath):
    try:
        local_size = os.path.getsize(filepath)
    except FileNotFoundError:
        local_size = 0
    return local_size


def delete_file(filepath):
    try:
        os.remove(filepath)
    except OSError:
        pass


def run_shell_command(command):
    result = subprocess.run(
        command, check=True
    )  # check to throw a Python Exception if an error happens
    return result.stdout


def download_file(url, filepath, remote_size, local_size):
    headers = {"Range": f"bytes={local_size}-"}
    response = requests.get(url, headers=headers, stream=True)
    with open(filepath, "ab") as f:
        with tqdm(
            total=remote_size,
            initial=local_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
                pbar.update(len(data))


def fetch_file(url, filepath):
    remote_size = get_remote_size(url)
    local_size = get_local_size(filepath)
    if local_size == 0:
        print(f'Found no local copy of "{filepath}". Starting the download.')
        download_file(url, filepath, remote_size, local_size)
    elif remote_size == 0:
        print(
            f"Found a local copy but couldn't determine the remote file size. Starting a fresh download to overwrite the possibly partial local file."
        )
        delete_file(filepath)
        local_size = 0
        download_file(url, filepath, remote_size, local_size)
    else:
        if remote_size == local_size:
            print(f'Found a full local copy of "{filepath}".')
        elif remote_size > local_size:
            print(f'Found a partial local copy "{filepath}". Resuming the download.')
            download_file(url, filepath, remote_size, local_size)
        else:
            print(
                f"Found a local copy but it is larger than the remote file. Starting a fresh download to overwrite the local file."
            )
            delete_file(filepath)
            local_size = 0
            download_file(url, filepath, remote_size, 0)


def validate_file(filepath, md5_hash):
    with open(filepath, "rb") as f:
        bytes = f.read()
    md5_hash_calc = hashlib.md5(bytes).hexdigest()
    if md5_hash == md5_hash_calc:
        print(f"MD5 checksum is correct.")
    else:
        print(
            f"MD5 checksum deviates from the expected one. The file could be corrupted from an incomplete download."
        )


def create_dir(dirpath):
    os.makedirs(dirpath, exist_ok=True)


# Extraction


def extract_tar_gz(filepath):
    print(f'Starting to extract "{filepath}".')
    directory = os.path.dirname(filepath)
    with tarfile.open(filepath, "r:gz") as tar:
        tar.extractall(path=directory)


# File loading


def read_csv_file(filepath):
    with open(filepath) as f:
        df = pd.read_csv(f, engine="pyarrow")  # optional engine that is faster
    return df


def read_json_file(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data


def read_tsv_file(filepath):
    with open(filepath) as f:
        df = pd.read_csv(f, sep="\t")
    return df


def read_tsv_file(filepath, header=0):
    with open(filepath) as f:
        df = pd.read_csv(f, sep="\t", low_memory=False, header=header)
    return df


def read_ttl_file(filepath):
    import rdflib  # local import because it's not often needed

    g = rdflib.Graph()
    g.parse(filepath, format="turtle")
    return g


# Graph construction
# - [Graph](https://igraph.org/python/doc/api/igraph.Graph.html)
# - [add_vertices](https://igraph.org/python/doc/api/igraph.Graph.html#add_vertices)
# - [add_edges](https://igraph.org/python/doc/api/igraph.Graph.html#add_edges)


def create_graph(nodes, edges):
    # Graph
    g = ig.Graph(directed=True)

    # Nodes
    ig_nodes = []
    ig_node_attributes = {"type": []}
    known_node_property_keys = set()
    for i, (node_id, node_type, node_properties) in enumerate(nodes):
        ig_nodes.append(node_id)
        ig_node_attributes["type"].append(node_type)
        known_node_property_keys.update(node_properties.keys())
        for key in known_node_property_keys:
            if key == "type":
                used_key = "_type"  # "type" is already used (node_type from entry in column 1) and can't be used if present in a node property
            elif key == "name":
                used_key = "_name"  # "name" has special meaning in igraph (used for identifying nodes) and can't be used if present in a node property
            else:
                used_key = key
            if used_key not in ig_node_attributes:
                ig_node_attributes[used_key] = [None] * i
            val = node_properties.get(key, None)
            ig_node_attributes[used_key].append(val)
    g.add_vertices(ig_nodes, ig_node_attributes)

    # Edges
    ig_edges = []
    ig_edge_attributes = {"type": []}
    known_edge_property_keys = set()
    for i, (source_id, target_id, edge_type, edge_properties) in enumerate(edges):
        edge_id = (source_id, target_id)
        ig_edges.append(edge_id)
        ig_edge_attributes["type"].append(edge_type)
        known_edge_property_keys.update(edge_properties.keys())
        for key in known_edge_property_keys:
            if key == "type":
                used_key = "_type"  # "type" is already used (edge_type from entry in column 1) and can't be used if present in a edge property
            elif key == "name":
                used_key = "_name"  # "name" has special meaning in igraph and isn't used if present in a edge property to be sure it doesn't interfere
            else:
                used_key = key
            if used_key not in ig_edge_attributes:
                ig_edge_attributes[used_key] = [None] * i
            val = edge_properties.get(key, None)
            ig_edge_attributes[used_key].append(val)
    g.add_edges(ig_edges, ig_edge_attributes)
    return g


# Data export


def export_nodes_as_csv(nodes, directory, basename, subgraph=None):
    num_nodes = len(nodes) if subgraph is None else subgraph.vcount()
    filename = f"{basename}_nodes_n{num_nodes}.csv"
    filepath = os.path.join(directory, filename)
    with open(filepath, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "type", "properties"])

        if subgraph is None:
            used_nodes = nodes
        else:
            used_nodes = filter_nodes_by_subgraph(nodes, subgraph)

        for node_id, node_type, node_properties in used_nodes:
            writer.writerow([str(node_id), str(node_type), json.dumps(node_properties)])
    return filepath


def export_edges_as_csv(edges, directory, basename, subgraph=None):
    num_edges = len(edges) if subgraph is None else subgraph.ecount()
    filename = f"{basename}_edges_e{num_edges}.csv"
    filepath = os.path.join(directory, filename)
    with open(filepath, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["source_id", "target_id", "type", "properties"])

        if subgraph is None:
            used_edges = edges
        else:
            used_edges = filter_edges_by_subgraph(edges, subgraph)

        for source_id, target_id, edge_type, edge_properties in used_edges:
            writer.writerow(
                [source_id, target_id, edge_type, json.dumps(edge_properties)]
            )
    return filepath


def export_graph_as_graphml(graph, directory, basename):
    n = graph.vcount()
    m = graph.ecount()
    filename = f"{basename}_graph_n{n}_e{m}.graphml"
    filepath = os.path.join(directory, filename)
    graph.write_graphml(filepath)
    return filepath


# Data filtering


def filter_nodes_by_subgraph(nodes, subgraph):
    node_ids = set([vertex["name"] for vertex in subgraph.vs])
    filtered_nodes = [node for node in nodes if node[0] in node_ids]
    return filtered_nodes


def filter_edges_by_subgraph(edges, subgraph):
    edge_ids = set(
        [
            (subgraph.vs[e.source]["name"], subgraph.vs[e.target]["name"], e["type"])
            for e in subgraph.es
        ]
    )
    filtered_edges = [edge for edge in edges if edge[0:3] in edge_ids]
    return filtered_edges


# Graph operations


def report_graph_stats(graph):
    n = graph.vcount()
    m = graph.ecount()
    density = graph.density(graph)
    directed = "directed" if graph.is_directed() else "undirected"
    multi = "multi" if graph.is_multiple() else ""
    print(
        f"{directed.title()} {multi}graph with {n} nodes, {m} edges and a density of {density:.4}."
    )


def list_nodes_matching_substring(graph, substring, target=None):
    substring = substring.lower()
    sep = 4

    if target is None:
        data = []
        id_max_len = type_max_len = 1
        for v in graph.vs:
            try:
                if substring in str(v["name"]).lower():
                    node_id = str(v["name"])
                    node_type = str(v["type"])
                    data.append((node_id, node_type))
                    if len(node_id) > id_max_len:
                        id_max_len = len(node_id)
                    if len(node_type) > type_max_len:
                        type_max_len = len(node_type)
            except Exception:
                pass
        id_len = id_max_len + sep
        type_len = type_max_len + sep
        print(f"{'id':<{id_len}}{'type':<{type_len}}")
        print("=" * (id_len + type_len))
        for node_id, node_type in sorted(data):
            print(f"{node_id:<{id_len}}{node_type:<{type_len}}")
    else:
        target = str(target)
        data = []
        id_max_len = type_max_len = property_max_len = 1
        for v in graph.vs:
            try:
                if substring in str(v[target]).lower():
                    node_id = str(v["name"])
                    node_type = str(v["type"])
                    node_property = str(v[target])
                    data.append((node_id, node_type, node_property))
                    if len(node_id) > id_max_len:
                        id_max_len = len(node_id)
                    if len(node_type) > type_max_len:
                        type_max_len = len(node_type)
                    if len(node_property) > property_max_len:
                        property_max_len = len(node_property)
            except Exception:
                pass
        id_len = id_max_len + sep
        type_len = type_max_len + sep
        property_len = property_max_len + sep
        print(f"{'id':<{id_len}}{'type':<{type_len}}{target:<{property_len}}")
        print("=" * (id_len + type_len + property_len))
        for node_id, node_type, node_property in sorted(data):
            print(
                f"{node_id:<{id_len}}{node_type:<{type_len}}{node_property:<{property_len}}"
            )


def get_egocentric_subgraph(graph, node_id):
    neighbors = graph.neighborhood(node_id)
    subgraph = graph.induced_subgraph(neighbors).copy()
    return subgraph


def get_paths_subgraph(graph, source, target):
    shortest_paths = graph.get_all_shortest_paths(source, target)
    edges = set()
    for path in shortest_paths:
        for i in range(len(path) - 1):
            s = path[i]
            t = path[i + 1]
            edge = (s, t)
            edges.add(edge)
    subgraph = graph.subgraph_edges(edges)
    return subgraph


def visualize_graph(graph, node_type_to_color=None, source=None, target=None):
    if node_type_to_color is None:
        node_type_to_color = {}

    # Graph
    g_vis = ig.Graph(directed=graph.is_directed())

    # Nodes
    def shorten(string, max_length):
        if len(string) > max_length:
            n = int(max_length / 2 - 3)
            string = string[:n] + " ... " + string[-n:]
        return string

    for node in graph.vs:
        node_id = node["name"]
        node_type = node["type"]
        node_properties = {
            k: node[k]
            for k in node.attribute_names()
            if k not in ["name", "type"] and node[k] not in [None, "", []]
        }
        node_properties_str = "\n".join(
            f" <b>{k}:</b> {shorten(str(v), 120)}"
            for k, v in sorted(node_properties.items())
        )
        hover = f"<b>id:</b>{node_id}\n<b>type:</b>{node_type}\n<b>properties:</b>\n{node_properties_str}"
        hover = shorten(hover, 1000)
        coords = {}
        size = None
        try:
            coords["x"] = node["x"]
            coords["y"] = node["y"]
        except Exception:
            pass
        if source is not None:
            try:
                if node.index == source or node["name"] == source:
                    coords["x"] = 0 if target is None else -500
                    coords["y"] = 0
                    size = 20
            except KeyError:
                pass
        if target is not None:
            try:
                if node.index == target or node["name"] == target:
                    coords["x"] = 0 if source is None else +500
                    coords["y"] = 0
                    size = 20
            except KeyError:
                pass

        g_vis.add_vertex(
            name=node["name"],
            hover=hover,
            click="$hover",
            color=node_type_to_color.get(node["type"], None),
            size=size,
            **coords,
        )

    # Edges
    for edge in graph.es:
        try:
            hover = edge["type"]
        except Exception:
            hover = None
        g_vis.add_edge(
            edge.source,
            edge.target,
            hover=hover,
        )

    # Visualization
    fig = gv.d3(
        g_vis,
        node_label_data_source="name",
        many_body_force_strength=-1500,
        edge_curvature=0.1,
        node_hover_neighborhood=True,
    )
    return fig
