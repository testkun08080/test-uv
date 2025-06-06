# Overview

This document summarizes various useful features of [UV](https://docs.astral.sh/uv/).
<!-- For those who have been using pip, the speed improvement is especially appreciated. -->

## Installation 💻

To install UV, run the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For more details, visit the [installation guide](https://docs.astral.sh/uv/getting-started/installation/).

---

## Quick Start: Sample Project

```bash
uv init heyhey-world
cd heyhey-world
uv run main.py
```

---

## Managing Virtual Environments and Modules (Without `.toml`)

### 1. Create a Virtual Environment

```bash
uv venv
```

*Specify Python version:*

```bash
uv venv --python 3.11
```

### 2. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 3. Add Modules

Install a module:

```bash
uv pip install requests
```

*Specify a version:*

```bash
uv pip install 'requests==2.31.0'
```

Install from `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

### 4. Remove Modules

```bash
uv pip uninstall requests
```

### 5. Export Installed Modules

```bash
uv pip freeze > requirements.txt
```

---

## Managing Virtual Environments and Modules (With `.toml`)

### 1. Initialize Project and Create a Virtual Environment

Initialize a new project:

```bash
uv init
uv venv
```

*With a custom name:*

```bash
uv init ProjectName
```

### 2. Add Modules

Add a module:

```bash
uv add requests
```

*Specify a version:*

```bash
uv add 'requests==2.31.0'
```

Install from `requirements.txt`:

```bash
uv add -r requirements.txt
```

### 3. Remove Modules

```bash
uv remove requests
```

### 4. Export Installed Modules

```bash
uv pip freeze > requirements.txt
```

---

## Setting Up from an Existing `.toml`

### 1. Sync Dependencies from `.toml`

```bash
uv sync
```

### 2. Run with Environment Variables

```bash
uv run --env-file=.env main.py
```

---

I hope this helps someone trying to use UV.