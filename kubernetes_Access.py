import csv
import pandas as pd
from kubernetes import client, config

# Function to load Kubernetes configuration (from kubeconfig file or in-cluster)
def load_k8s_config():
    try:
        # Try loading the kubeconfig from the default location (e.g., ~/.kube/config)
        config.load_kube_config()
    except Exception as e:
        print(f"Error loading Kubernetes config: {e}")
        exit(1)

# Function to fetch pod data from Kubernetes cluster
def fetch_pod_data():
    # Create the Kubernetes API client for Pod resources
    v1 = client.CoreV1Api()
    
    # Fetch pod information across all namespaces
    pod_list = v1.list_pod_for_all_namespaces(watch=False)
    
    # Prepare a list of dictionaries to store pod data
    pod_data = []
    for pod in pod_list.items:
        pod_data.append({
            "namespace": pod.metadata.namespace,
            "name": pod.metadata.name,
            "status": pod.status.phase,
            "created_at": pod.metadata.creation_timestamp,
            "node_name": pod.spec.node_name,
        })
    
    return pod_data

# Function to write data to a CSV file
def write_data_to_csv(data, filename):
    # Define column headers
    headers = ["namespace", "name", "status", "created_at", "node_name"]
    
    # Open CSV file in write mode and write the data
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to {filename}")

# Function to read data from the CSV file and load it into a Pandas DataFrame
def read_data_from_csv(filename):
    # Use Pandas to read the CSV file into a DataFrame
    df = pd.read_csv(filename)
    return df

# Main function to run the process
def main():
    # Load Kubernetes configuration
    load_k8s_config()

    # Fetch pod data from Kubernetes
    pod_data = fetch_pod_data()

    # Write the pod data to a CSV file
    csv_filename = 'k8s_pod_data.csv'
    write_data_to_csv(pod_data, csv_filename)

    # Read the data back from the CSV file using Pandas
    df = read_data_from_csv(csv_filename)
    
    # Print the DataFrame to see the loaded data
    print("\nData extracted from the CSV file:")
    print(df)

# Run the main function
if __name__ == "__main__":
    main()
