# nearai-starter
NEAR AI Starter

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/near-agent/nearai-starter)

## Install

```bash
# Install nearai CLI. Recommend to use python 3.11
pip install nearai

# Show nearai CLI version
nearai version
```

## Login

```bash
# Sign login message with your NEAR account
# The login info will be available under ~/.nearai/registry/config.json
nearai login

# Set the `NEAR_ACCOUNT` env
NEAR_ACCOUNT=<your-near-account>  # e.g. alice.near
```

## Clone the repo

```bash
git clone https://github.com/near-agent/nearai-starter
cd nearai-starter

# Rename the folder ncd-cn.near to your NEAR account
mv ncd-cn.near $NEAR_ACCOUNT
```

## Deploy agent

After modifying `agent.py` and `metadata.json` under $NEAR_ACCOUNT/einstein, try to deploy your agent code.

```bash
# Deploy agent metadata and code to registry
nearai registry upload $NEAR_ACCOUNT/einstein

# Open the agent on NEAR AI
open https://app.near.ai/agents/$NEAR_ACCOUNT/einstein
```
