# data-annotation-usability-tests

Welcome to the usability tests annotation platform, a project for ECSE 542! The goal is to test various features of the annotation platform, to understand what factors about the platform improve users' annotation speeds and accuracy.

Project Notes:
In this folder, we have included
- Screenshots of the current state of the platform (simple task selection and data entry panel)
- Sketches
- Interview scripts

## Set Up + Usage

### Setting Up

To set up the environment, run the following commands

```bash
conda create -n annotate python=3.10
conda activate annotate
pip install -r requirements.txt
```

To run the app in a browser, run:

```bash
streamlit run main.py
```

### Creating a New Task

To add a task:

1. Add a CSV file for the raw file under `raw/` named as `<task_name>.csv`.

* Be sure the CSV file has a `label` column where the annotator's response will be added!

2. Create a `<task_name>.py` file under `pages/` which provides the interface for annotation

3. Update the `assets/task_metadata.json` by adding a dictionary containing the path to the python file and display name.

### Creating a User

Add the name, email, username, and password of a new user to the `assets/config.yaml` file

### Assigning a User to a Task

Run the `assign.py` script, which works as follows. If this is the user's first task, a folder with metadata will be created for them in the process.

```bash
python assign.py --username john --task qa
```

We can also assign shared tasks, meaning that multiple people can contribute to annotating one dataset. To do this, set the username as `shared`.
