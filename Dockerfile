FROM python:3.11.4

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install xdg-utils python3-venv -y

# Install Node 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

# Install AWS Amplify CLI & Vite
RUN npm install -g @aws-amplify/cli && npm install -g vite@latest

# Install AWS CLI & other tools
RUN pip install awscli pipenv aws_lambda_powertools boto3 botostubs
RUN pip install --upgrade pip

WORKDIR /workspace
