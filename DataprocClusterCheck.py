from google.cloud import dataproc_v1 
from google.cloud.dataproc_v1 import ClusterControllerClient
from google.api_core import client_options,operations_v1

api_endpoint = "us-central1-dataproc.googleapis.com:443"
options = client_options.ClientOptions(
    api_endpoint=api_endpoint,
)
# Create a client object for the Dataproc API
client = dataproc_v1.ClusterControllerClient(client_options=options,)

# Set the project ID, region, and cluster name for the Dataproc cluster
req = dataproc_v1.GetClusterRequest(
    project_id="<project-id>",
    region="us-central1",
    cluster_name="<Cluster-Name>",
)

# Create a request to get the cluster status
response = client.get_cluster(request=req)

# Check if the cluster is running and the NameNode is active
# ref https://cloud.google.com/python/docs/reference/dataproc/5.4.0/google.cloud.dataproc_v1.types.ClusterStatus.State
if response.status.state.value == 2:
    print("NameNode is active")
else:
    print("NameNode is not active")
