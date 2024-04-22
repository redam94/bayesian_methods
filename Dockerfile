FROM python:3.11 as build
# Install the modules specified in the requirements.txt
RUN apt-get update && apt-get install -y \
   && apt-get install -y cmake build-essential gcc gfortran libopenblas-dev ca-certificates lsb-release wget libhdf5-dev

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

FROM python:3.11-slim as runtime
WORKDIR /app
COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY /app /app
EXPOSE 8501
# The command that run the app
CMD streamlit run Home.py --server.address 0.0.0.0 --server.port 8501