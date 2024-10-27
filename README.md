# data-annotation-usability-tests

Welcome to the usability tests annotation platform, a project for ECSE 542! The goal is to test various features of the annotation platform, to understand what factors about the platform improve users' annotation speeds and accuracy.

## Milestone Logs

### Milestone 1

* Created basic annotation set up, where users are shown a sequence of data samples to annotate
* On the admin side, it contains features that allows me to assign users to tasks

In the submission, we included:
- Screenshots of the current state of the platform (simple task selection and data entry panel)
- Sketches
- Interview scripts

### Milestone 2

* Created multiple pages and tweaked the scripts so that (1) a user gets assigned all tasks to be tested, and (2) the task page lets users choose which task to work on
* Tweaked the 6 pages to match the 6 changes in interfaces that we want to test, namely:
  * Interface 1: Plain, white background
  * Interface 2: Dark mode
  * Interface 3: Large font
  * Interface 4: Serif font
  * Interface 5: 10 second lag between samples
  * Interface 6: 30 second lag between samples

In the submission, we included:
- Screenshots of the 5 interfaces
- Updated codebase

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
