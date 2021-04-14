# Airflow-base

Base image for Apache airflow

## Quick Run

```bash
docker build -t airflow-base . \
&& docker run \
-p 8080:8080 \
-v $(pwd):/usr/local/airflow/dags \
--name airflow \
airflow-base

```

