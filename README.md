# Automation [![Python Version](https://img.shields.io/badge/python-3.6.1-brightgreen.svg?)](https://www.python.org/downloads/)

Collection of automated tasks.

> **Disclaimer**: Some of the scripts are small and may not be very useful for example [Send-email](https://github.com/endormi/automation/blob/master/send-email/email.py), but are still pretty cool :).

> I created some of the scripts with the intention that they're a foundation for more complex automated scripts such as. expenses, income, selenium-testing and a few more. The files that are these types of scripts will have (X).

Clone repository:

```
git clone https://github.com/endormi/automation.git
```

Install requirements:

```sh
pip install -r requirements.txt
```

Now you can run every script.

- [DL-file](https://github.com/endormi/automation/blob/master/dl-file/dl.py) - X - File downloader.
- [Excel](https://github.com/endormi/automation/blob/master/excel):
  - [Expenses](https://github.com/endormi/automation/blob/master/excel/expenses.py) - X - Adds business and personal expenses to Excel (Current code needs you to add the expenses manually, but will automatically add them to Excel. Not ideal I know, I'll be adding a better code when I have time). This is only a foundation for your excel files, which you can then update to your own liking.
  - [Graph](https://github.com/endormi/automation/blob/master/excel/graphs.py) - X - Excel graph.
  - [Income](https://github.com/endormi/automation/blob/master/excel/income.py) - X - Adds income to Excel (Current code needs you to add the income manually, but will automatically add them to Excel. Not ideal I know, I'll be adding a better code when I have time). This is only a foundation for your excel files, which you can then update to your own liking.
- [Hue-light](https://github.com/endormi/automation/blob/master/hue-light/control.py) - X - Control hue lights.
- [Git-commands](https://github.com/endormi/automation/blob/master/git-commands/commands.py) - Automates the process of using commands such as clone, commit, branch, pull, merge and blame.
- [Monitor-website](https://github.com/endormi/automation/blob/master/monitor-website/web.py) - If website isn't up-and-running, sends an email and plays a sound.
- [Move-cursor](https://github.com/endormi/automation/blob/master/move-cursor/cursor.py) - Move cursor every 10 seconds.
- [Organize-files](https://github.com/endormi/automation/blob/master/organize-files/organizer.py) - Organizes files (images, audio, texts, videos and compressed files) and moves them inside specified folders.
- [Repo](https://github.com/endormi/automation/tree/master/repo) - Creates a private or public GitHub repository (uses selenium, but you can easily also use the GitHub package).
- [Scheduler](https://github.com/endormi/automation/tree/master/scheduler/scheduler.py) - X - Scheduled jobs (open email, shutdown computer etc.).
- [Selenium testing](https://github.com/endormi/automation/tree/master/selenium-testing):
  - [Cross browser](https://github.com/endormi/automation/blob/changes/selenium-testing/cross-browser.py) - X - Cross browser testing.
  - [Login form](https://github.com/endormi/automation/blob/changes/selenium-testing/login-form.py) - X - Login form testing (tests GitHub, Stack Overflow and Twitter) and generates report.
  - [Search](https://github.com/endormi/automation/blob/changes/selenium-testing/search.py) - X - Search function testing (searches `Python` in GitHub, Stack Overflow and Amazon) and generates report.
  - [Sign up SO](https://github.com/endormi/automation/blob/changes/selenium-testing/sign-up-so.py) - X - Sign up testing (tests Stack Overflow, Gmail and GitHub) and generates report.
- [Send-email](https://github.com/endormi/automation/blob/master/send-email/email.py) - Send emails (subject, content and image attachments).
- [Tweeter](https://github.com/endormi/automation/blob/master/tweeter) - Write and post tweets.
- [Whatsapp](https://github.com/endormi/automation/blob/master/whatsapp/msg.py) - Send Whatsapp message (I'm thinking of switching from Whatsapp, but thought this still should be added).
- [Youtube](https://github.com/endormi/automation/blob/master/youtube/dl.py) - Download an audio from YouTube.

## License

The source code is released under the [MIT License](https://github.com/endormi/automation/blob/master/LICENSE).
