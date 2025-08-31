# dataduck



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.intelligentb.com/cafu/data-engineering/dataduck.git
git branch -M master
git push -uf origin master
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.intelligentb.com/cafu/data-engineering/dataduck/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

# 🦆 Data-Duck

Welcome to **Data-Duck** – the quackiest way to run Python functions from a web UI! 🦆💻

## What is Data-Duck?
Data-Duck is a web-based tool that lets you create, run, and monitor Python functions (tasks) with the grace of a duck gliding across a pond. No more command-line flapping – just click, upload, and watch your code take flight!

---

## 🛠️ How to Add a New Python Function (Task) to the UI

1. **Write Your Python Function:**
   - Waddle over to the `task_workers/` folder.
   - Create a new `.py` file or add your function to an existing one.
   - Your function should be a generator (it should `yield` progress updates, because ducks like to keep you posted).

   Example:
   ```python
   def my_cool_task(param1, param2):
       yield f"Starting with {param1} and {param2}!"
       # ...do stuff...
       yield ("Success", "All done! 🦆")
   ```

2. **Register Your Function in `task_execution.py`:**
   - Open `task_execution.py`.
   - Add your function to the `task_functions` dictionary in `stream_task_execution`.
   - Example:
     ```python
     from task_workers.my_worker import my_cool_task
     task_functions = {
         'My Cool Task': my_cool_task,
         # ...other tasks...
     }
     ```

3. **Add Task Parameters in `task_parameters.py`:**
   - Open `task_parameters.py`.
   - Add an entry for your task in the `task_parameters` dictionary.
   - Example:
     ```python
     'My Cool Task': [
         {'name': 'param1', 'type': 'text', 'label': 'Parameter 1'},
         {'name': 'param2', 'type': 'text', 'label': 'Parameter 2'},
     ],
     ```

4. **Add Your Task to the YAML File:**
   - Open `task_list.yaml`.
   - Add your task under the appropriate category.
   - Example:
     ```yaml
     My Category:
       - id: 'My Cool Task'
         name: 'My Cool Task'
         description: 'Does something really cool!'
     ```

5. **Restart the App:**
   - Give your feathers a shake and restart the Flask app. Your new task will appear in the UI, ready to quack!

---

## 📝 Editing the YAML File
- The `task_list.yaml` file is where you organize your tasks into categories.
- Each task needs an `id`, `name`, and `description`.
- Don’t forget: YAML is picky about spaces. Ducks are not, but YAML is.

---

## 🦆 Why Data-Duck?
- Because ducks are awesome.
- Because web UIs are easier than command lines.
- Because you deserve to have fun while running Python code.

---

## 💡 Pro Tips
- If you see an error, don’t panic – just keep calm and quack on.
- Want to add a file upload? Set the parameter type to `file` in `task_parameters.py`.
- Ducks love progress bars. Make your function yield lots of updates!

---

Happy coding, and may your data always float! 🦆
## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
