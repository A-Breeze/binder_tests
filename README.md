[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/A-Breeze/binder_tests/conda_pip?urlpath=lab)

# binder_tests
Tests to get Binder working. Specifically, working through the following resources to in an attempt to get the following functionality to work:
1. Basic **conda environment** specified by an `environment.yml`: <https://github.com/binder-examples/conda>. Also included:
    1. Using **JupyterLab**
    1. Using **Git** in the Terminal of JupyterLab to commit and push/pull from the remote on GitHub
2. Add **JupyterLab extensions** by commands in the `postBuild` file for Binder <https://github.com/binder-examples/jupyterlab/blob/master/binder/postBuild> and <https://github.com/mwouts/jupytext/blob/master/binder/postBuild>. Included:
    1. **Jupytext**
    1. **Table of Contents**
    1. **Offline notebook** to allow you to easily download a notebook.
3. Further dependencies specified in a conda environment:
    1. Call **pip** `requirements.txt` from the `environment.yml` (see `conda` example [here]<https://github.com/conda/conda/blob/master/tests/conda_env/support/advanced-pip/environment.yml>).
    1. Install standard data science packages: **numpy**, **pandas**, **scikit-learn**, **matplotlib**

## Limitations found
1. Jupyter does not (by default) show *hidden* files and folders (i.e. whose name begins with a dot `.`) in the file explorer, e.g. `.gitignore`. This is an open issue, see: <https://github.com/jupyterlab/jupyterlab/issues/2049>.
1. Binder includes various hidden files in the project root folder (that have not been specified in the repo). I decided to ignore these for the purpose of the repo (on the basis that they are generated from the other files).
    - To list all files and folders from a JupyterLab Terminal: `$ ls -al`
    - To open a *hidden* file from JupyterLab: `File` - `Open from path...`.
1. Security is *not* guaranteed for pushing changes from Binder to the GitHub remote repo. That is, **do not enter your GitHub credentials** (which are required to push) to Binder (e.g. in the Terminal of JupyterLab). As per: <https://mybinder.readthedocs.io/en/latest/faq.html#can-i-push-data-from-my-binder-session-back-to-my-repository>. 
    
    Workaround (a bit manual, but there is not another way):
    - Have a cloned copy of the repo on your local machine.
    - Amend files in Binder. When you want to make a commit, download the files that have changed and replace them in the local machine's clone.
    - Commit from local and push to remote.
    - Pull from Binder Terminal. (You will probably first need to `git reset --hard HEAD` or at least `stash` because you'll be trying to overwrite files that have changed.)
1. Binder has limited computation resources. Specifically:
    > Users are guaranteed at least 1GB of RAM, with a maximum of 2GB
    
    As per: <https://mybinder.readthedocs.io/en/latest/faq.html#how-much-memory-am-i-given-when-using-binder>
1. The Binder configuration files must all be in the same directory, e.g. you *cannot* have `./environment.yml` (in the root) and `./binder/postBuild` (in a subfolder).
1. The jupytext extension for JupyterLab requires JupyterLab 2.0, and the Binder default version for JupyterLab was 1.2.6 when I tried it (that's the most recent version that is in Anaconda Cloud, but there are more recent versions on conda-forge), so you need to specify a more up-to-date version of JupyterLab in the `environment.yml`.

## Further notes
### JupyterLab extensions
We can specify specific versions of JupyterLab extensions in the commands run in the `postBuild` file. This is required if the default versions that Binder uses are not compatible for some reason. Commands are:
```
> jupyter labextension --help  # To see available commands
> jupyter labextension install my-extension  # Install an extension...
> jupyter labextension install my-extension@1.2.3  # ...at a specific version
> jupyter labextension list  # See which extensions and versions are installed
> npm search my-extension  # Look for the npm package containing "my-extension"
> npm view my-extension versions  # Get a list of all available versions of a package
```
See <https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#installing-extensions> and <https://stackoverflow.com/q/41415945>.



