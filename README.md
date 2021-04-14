# Airflow-base

Base image for Apache airflow

## Quick Run

```bash
docker build -t airflow-base . \
&& docker run \
-p 8080:8080 \
-v /Users/dexter/Projects/airflow-base/dags:/usr/local/airflow/dags \
-v /Users/dexter/Projects/airflow-base/requirements.txt:/requirements.txt \
--name qrobo_airflow \
airflow-base

```

