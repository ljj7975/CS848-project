# CS848-project

---

## Submitting Spark job

1) download spark from http://apache.forsale.plus/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz and unzip

2) build jar by running `mvn clean package` under `CS848-project`

3) add your jar to `spark-2.4.0-bin-hadoop2.7/examples/jars`

4) build docker image of spark using `./bin/docker-image-tool.sh -r <docker_hub_id> -t <tag_name> build`

5) push docker image of spark using `./bin/docker-image-tool.sh -r <docker_hub_id> -t <tag_name> push`

6) ssh into tem101 (or tem102)

7) download spark from http://apache.forsale.plus/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz and unzip on tembo

8) run job with following command format
```
bin/spark-submit \
    --master k8s://https://192.168.152.201:6443 \
    --deploy-mode cluster \
    --name <job_name> \
    --class <class_name> \
    --conf spark.executor.instances=5 \
    --conf spark.kubernetes.container.image=<image_name>:<image_tag> \
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
    local:///opt/spark/examples/jars/<jar_name>.jar <input>
```
&nbsp;&nbsp;&nbsp;&nbsp; note that class_name, image_name, image_tag, jar_name must be correctly provided. `/opt/spark/examples/jars/<jar_name>.jar` is location of target jar in the docker image

&nbsp;&nbsp;&nbsp;&nbsp; to run WordCount example,
```
bin/spark-submit \
    --master k8s://https://192.168.152.201:6443 \
    --deploy-mode cluster \
    --name word-count \
    --class cs848.wordcount.WordCount \
    --conf spark.executor.instances=5 \
    --conf spark.kubernetes.container.image=ljj7975/spark:ip \
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
    local:///opt/spark/examples/jars/cs848-project-1.0-SNAPSHOT.jar \
```

&nbsp;&nbsp;&nbsp;&nbsp; `192.168.152.202` can also be used

8) Once driver status has changed to Completed, `kubectl logs <spark_driver_pod_id>` to see logs


Refer following links for detail
- https://spark.apache.org/docs/latest/running-on-kubernetes.html
- https://weidongzhou.wordpress.com/2018/04/29/running-spark-on-kubernetes/

---

## Accessing files in HDFS through Spark

Must contact namenode which runs on tem103 (192.168.152.203).
Therefore, url is `hdfs://192.168.152.203/<path_to_file>` as in `sc.textFile("hdfs://192.168.152.203/test/20/0005447.xml")`

Noe that providing machine name like `node3` does not work.


## OpenNLP

Run with

```
mvn clean package
spark-submit --class cs848.nlp.NLPDriver target/cs848-project-1.0-SNAPSHOT.jar --input sample_text.txt
```

1) Sentence Detection on Solr Docs

```
spark-submit --class cs848.nlp.NLPDriver target/cs848-project-1.0-SNAPSHOT.jar --solr --search "search-term"
```

2) Sentence Detection on Text Files

```
spark-submit --class cs848.nlp.NLPDriver target/cs848-project-1.0-SNAPSHOT.jar --input "file-path"
```
