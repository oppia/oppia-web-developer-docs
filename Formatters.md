## Frontend

We use [prettier](https://prettier.io/) to format frontend code. It is configured based on [gts](https://github.com/google/gts). It is run as a pre-commit hook, i.e. it is executed every time you make a commit.

You can set up a prettier [extension](https://github.com/prettier/prettier-vscode) for vscode as well to format files when saving. Execute `npx prettier . --write` to format the code manually from the terminal.

Also, if you're using VSCode, here is a `.vscode/settings.json` that you can use:

```
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "prettier.configPath": "./.prettierrc.json",
  "prettier.ignorePath": "./.prettierignore",
  "git.ignoreLimitWarning": true
}
```
