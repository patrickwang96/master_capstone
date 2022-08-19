
#FROM python:buster as build-image
FROM ibmfunctions/action-python-v3.7

# Update and install curl. 
RUN apt update
RUN apt install -y curl build-essential moreutils expect# stdbuf

# Define and create function directory
ENV FUNCTION_DIR="/var/task"
RUN mkdir -p ${FUNCTION_DIR}

# Copy function code
COPY . ${FUNCTION_DIR}

# RUN pip install boto3 botocore

# # Install the runtime interface client
# RUN pip install \
#         --target ${FUNCTION_DIR} \
#         awslambdaric



# Set working directory
WORKDIR ${FUNCTION_DIR}

# Compile C code
# RUN gcc -o stream.10M -O -DSTREAM_ARRAY_SIZE=10000000 -DNTIMES=10 stream_small.c
RUN cd ${FUNCTION_DIR}/llcbench  && make clean && make cache-bench 
# RUN gcc cpu_bound.c -o cpu_bound


# Set entry script that determines whether to run RIE if running locally
# COPY ./entry_script.sh /entry_script.sh
# RUN chmod +x /entry_script.sh
# ENTRYPOINT [ "/entry_script.sh" ]

# Set handler
# CMD [ "lambda_function.lambda_handler" ]
