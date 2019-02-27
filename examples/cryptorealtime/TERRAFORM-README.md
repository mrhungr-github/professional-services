#Terraform template

###Get the BTC-USD realtime periscope multi exchange observer running  in less than 10 minutes

![Architectural overview](crypto.gif)


###Terraform version used in this tutorial: v0.11.11 

###Providers used:
- provider.google v1.20.0


###Setup:
- Open the Terraform Shell and clone the project
```console 
git clone https://github.com/galic1987/professional-services/ 
cd professional-services/examples/cryptorealtime/terraform-setup/
```

- Fill out the [terraform.tfvars](terraform-setup/terraform.tfvars) configuration
```console 
 vim terraform.tfvars 
 ```

- Check that everything is working 
```console 
terraform init
terraform apply 
```
(ignore api enablement errors and/or rerun)

- Wait 5-10 minutes until the VM startup script is booted 
- Note: Your public IP address will be displayed here or in console 

- SSH into the VM that was [created](https://console.cloud.google.com/compute/instances)
```console 
sudo -s 
cd ~/professional-services/examples/cryptorealtime/
```


- Verify the variables from terraform are in place:
```console 
echo "PROJECT_ID" $PROJECT_ID  "REGION" $REGION "ZONE" $ZONE "BUCKET_NAME" $BUCKET_NAME "BUCKET_FOLDER" $BUCKET_FOLDER "BIGTABLE_INSTANCE_NAME" $BIGTABLE_INSTANCE_NAME "BIGTABLE_TABLE_NAME" $BIGTABLE_TABLE_NAME "BIGTABLE_FAMILY_NAME" $BIGTABLE_FAMILY_NAME 
```

```console 
cat verify.txt
```

- Run the dataflow job to connect to exchanges
```console 
./run.sh ${PROJECT_ID} ${BIGTABLE_INSTANCE_NAME} ${BUCKET_NAME}${BUCKET_FOLDER} ${BIGTABLE_TABLE_NAME} $BIGTABLE_FAMILY_NAME
``` 
- Ignore any *java.lang.IllegalThreadStateException*


- Go to frontend script and run the frontend flask server and data visualisation
```console 
cd frontend/
python app.py ${PROJECT_ID} ${BIGTABLE_INSTANCE_NAME} ${BIGTABLE_TABLE_NAME} ${BIGTABLE_FAMILY_NAME}
```

- Open the VM IP on port 5000 in your browser to see the chart 


**Cleanup:**
- Navigate to the Terraform shell
- We have to delete the Cloud Bigtable instances manually because there is a bug in the current Terraform provider
```console 
gcloud bigtable instances delete cryptobackend-bigtable
terraform state rm google_bigtable_instance.instance
```

- Delete the Dataflow jobs
```console 
gcloud dataflow jobs cancel \
$(gcloud dataflow jobs list \
--format='value(id)' \
--filter="name:runthepipeline*")
``` 

- Take down the infrastructure 
```console 
terraform destroy
```

Read [the post](https://medium.com/p/bigtable-beam-dataflow-cryptocurrencies-gcp-terraform-java-maven-4e7873811e86/edit) for addtional information:


![Terraform](https://media.giphy.com/media/sDjIG2QtbXKta/giphy.gif)
