# Professional Services
Common solutions and tools developed by Google Cloud's Professional Services team.

## Examples
The examples folder contains example solutions across a variety of Google Cloud Platform products. Use these solutions as a reference for your own or extend them to fit your particular use case.

* [BigQuery Audit Log](examples/bigquery-audit-log) - Solution to help audit BigQuery usage using Data Studio for visualization and a sample SQL script to query the back-end data source consisting of audit logs.
* [BigQuery Cross Project Slot Monitoring](examples/bigquery-cross-project-slot-monitoring) - Solution to help monitoring slot utilization across multiple projects, while breaking down allocation per project.
* [BigQuery Group Sync For Row Level Access](examples/bigquery-row-access-groups) - Sample code to synchronize group membership from G Suite/Cloud Identity into BigQuery and join that with your data to control access at row level.
* [Cloud Composer Examples](examples/cloud-composer-examples) - Examples of using Cloud Composer, GCP's managed Apache Airflow service.
* [Cloud Dataflow and Cloud Bigtable Cyptocurrencies Exchange Realtime Example](examples/cryptorealtime) - Apache Beam example that reads from the Crypto Exchanges WebSocket API and saves the feed in Cloud Bigtable. Real time visualization from Bigtable running on Flask server are included.
* [CloudML Bank Marketing](examples/cloudml-bank-marketing) - Notebook for creating a classification model for marketing using CloudML.
* [CloudML Bee Health Detection](examples/cloudml-bee-health-detection) - Detect if a bee is unhealthy based on an image of it and its subspecies.
* [CloudML Energy Price Forecasting](examples/cloudml-energy-price-forecasting) - Predicting the future energy price based on historical price and weather.
* [CloudML Fraud Detection](examples/cloudml-fraud-detection) - Fraud detection model for credit-cards transactions.
* [CloudML Sentiment Analysis](examples/cloudml-sentiment-analysis) - Sentiment analysis for movie reviews using TensorFlow `RNNEstimator`.
* [CloudML TensorFlow Profiling](examples/tensorflow-profiling-examples) - TensorFlow profiling examples for training models with CloudML
* [Dataflow BigQuery Transpose Example](examples/dataflow-bigquery-transpose) - An example pipeline to transpose/pivot/rotate a BigQuery table.
* [Dataflow Elasticsearch Indexer](examples/dataflow-elasticsearch-indexer) - An example pipeline that demonstrates the process of reading JSON documents from Cloud Pub/Sub, enhancing the document using metadata stored in Cloud Bigtable and indexing those documents into [Elasticsearch](https://www.elastic.co/).
* [Dataflow Python Examples](examples/dataflow-python-examples) - Various ETL examples using the Dataflow Python SDK.
* [Dataflow Scala Example: Kafka2Avro](examples/dataflow-scala-kafka2avro) - Example to read objects from Kafka, and persist them encoded in Avro in Google Cloud Storage, using Dataflow with SCIO.
* [Dataflow Template Pipelines](https://github.com/GoogleCloudPlatform/DataflowTemplates) - Pre-implemented Dataflow template pipelines for solving common data tasks on Google Cloud Platform.
* [Data Generator](examples/dataflow-data-generator) - Generate random data with a custom schema at scale for integration tests or demos.
* [Dataflow Streaming Benchmark](examples/dataflow-streaming-benchmark) - Utility to publish randomized fake JSON messages to a Cloud Pub/Sub topic at a configured QPS.
* [DLP API Examples](examples/dlp) - Examples of the DLP API usage.
* [Home Appliance Status Monitoring from Smart Power Readings](examples/e2e-home-appliance-status-monitoring) - An end-to-end demo system featuring a suite of Google Cloud Platform products such as IoT Core, ML Engine, BigQuery, etc.
* [IoT Nirvana](examples/iot-nirvana) - An end-to-end Internet of Things architecture running on Google Cloud Platform.
* [Kubeflow Pipelines Sentiment Analysis](examples/kubeflow-pipelines-sentiment-analysis) - Create a Kubeflow Pipelines component and pipelines to analyze sentiment for New York Times front page headlines using Cloud Dataflow (Apache Beam Java) and Cloud Natural Language API.
* [Pub/Sub Client Batching Example](examples/pubsub-publish-avro-example) - Batching in Pub/Sub's Java client API.
* [QAOA](examples/qaoa) - Examples of parsing a max-SAT problem in a proprietary format.
* [Redis Cluster on GKE Example](examples/redis-cluster-gke) - Deploying Redis cluster on GKE.
* [Spinnaker](examples/spinnaker) - Example pipelines for a Canary / Production deployment process.

## Tools
The tools folder contains ready-made utilities which can simpilfy Google Cloud Platform usage.


* [BigQuery Committed Use Discounts (CUD)/Sustained Use Discounts (SUD) Per-project Attribution](tools/kunskap) - A tool that automates the generation of a Bigquery table that uses existing exported billing data, by attributing both CUD and SUD charges on a per-project basis.
* [AssetInventory](tools/asset-inventory) - Import Cloud Asset Inventory resourcs into BigQuery.
* [BigQuery Committed Use Discounts (CUD)/Sustained Use Discounts (SUD) Per-project Attribution](tools/kunskap) - A tool that automates the generation of a Bigquery table that uses existing exported billing data, by attributing both CUD and SUD charges on a per-project basis.
* [CloudConnect](tools/cloudconnect) - A package that automates the setup of dual VPN tunnels between AWS and GCP.
* [Cloudera Parcel GCS Connector](tools/cloudera-parcel-gcsconnector) - This script helps you create a Cloudera parcel that includes Google Cloud Storage connector. The parcel can be deployed on a Cloudera managed cluster.
This script helps you create a Cloudera parcel that includes Google Cloud Storage connector. The parcel can be deployed on a Cloudera managed cluster.
* [DNS Sync](tools/dns-sync) - Sync a Cloud DNS zone with GCE resources. Instances and load balancers are added to the cloud DNS zone as they start from compute_engine_activity log events sent from a pub/sub push subscription. Can sync multiple projects to a single Cloud DNS zone.
* [GCE Quota Sync](tools/gce-quota-sync) - A tool that fetches resource quota usage from the GCE API and synchronizes it to Stackdriver as a custom metric, where it can be used to define automated alerts.
* [GCP Architecture Visualizer](/tools/gcp-arch-viz) - A tool that takes CSV output from a Forseti Inventory scan and draws out a dynamic hierarchical tree diagram of org -> folders -> projects -> gcp_resources using the D3.js javascript library.
* [GCS Bucket Mover](tools/gcs-bucket-mover) - A tool to move user's bucket, including objects, metadata, and ACL, from one project to another.
* [GKE Billing Export](tools/gke-billing-export) - Google Kubernetes Engine fine grained billing export.
* [GSuite Exporter](tools/gsuite-exporter/) - A Python package that automates syncing Admin SDK APIs activity reports to a GCP destination. The module takes entries from the chosen Admin SDK API, converts them into the appropriate format for the destination, and exports them to a destination (e.g: Stackdriver Logging).
* [LabelMaker](tools/labelmaker) - A tool that reads key:value pairs from a json file and labels the running instance and all attached drives accordingly.
* [Maven Archetype Dataflow](tools/maven-archetype-dataflow) - A maven archetype which bootstraps a Dataflow project with common plugins pre-configured to help maintain high code quality.
* [Netblock Monitor](tools/netblock-monitor) - An Apps Script project that will automatically provide email notifications when changes are made to Google’s IP ranges.
* [Site Verification Group Sync](tools/site-verification-group-sync) - A tool to provision "verified owner" permissions (to create GCS buckets with custom dns) based on membership of a Google Group.

## Contributing
See the contributing [instructions](/CONTRIBUTING.md) to get started contributing.

## License
All solutions within this repository are provided under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license. Please see the [LICENSE](/LICENSE) file for more detailed terms and conditions.

## Disclaimer
This repository and its contents are not an official Google Product.

## Contact
Questions, issues, and comments should be directed to
[professional-services-oss@google.com](mailto:professional-services-oss@google.com).
