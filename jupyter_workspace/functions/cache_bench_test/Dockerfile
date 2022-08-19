
#FROM python:buster as build-image
FROM python:3.8-slim-buster

# Update and install curl. 
RUN apt update
RUN apt install -y curl build-essential moreutils expect #stdbuf

# Define and create function directory
ENV FUNCTION_DIR="/var/task"
RUN mkdir -p ${FUNCTION_DIR}

# Copy function code
COPY . ${FUNCTION_DIR}

RUN pip install boto3 botocore

# Install the runtime interface client
RUN pip install \
        --target ${FUNCTION_DIR} \
        awslambdaric

# Install the runtime interface emulator
RUN curl -Lo /usr/local/bin/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie
RUN chmod +x /usr/local/bin/aws-lambda-rie

# Set working directory
WORKDIR ${FUNCTION_DIR}

# Compile C code
# RUN gcc -o stream.10M -O -DSTREAM_ARRAY_SIZE=10000000 -DNTIMES=10 stream_small.c
RUN cd ${FUNCTION_DIR}/llcbench  && make clean && make cache-bench 


# Set entry script that determines whether to run RIE if running locally
COPY ./entry_script.sh /entry_script.sh
RUN chmod +x /entry_script.sh
ENTRYPOINT [ "/entry_script.sh" ]

# Set handler
CMD [ "lambda_function.lambda_handler" ]
