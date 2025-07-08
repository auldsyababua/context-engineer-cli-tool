# Claude Memory File - PROJECT_NAME

## ⚠️ CRITICAL PROTECTION RULES

### 🚫 NEVER MODIFY THE .claude DIRECTORY 🚫

The `.claude/` directory and its contents are PROTECTED and must NEVER be modified:

- **DO NOT** edit, delete, or modify `.claude/commands/` directory
- **DO NOT** edit, delete, or modify `.claude/settings.local.json`
- **DO NOT** create new files in `.claude/` directory
- **DO NOT** rename or move files in `.claude/` directory

These files are critical for Claude Code command functionality and project workflow.

### Protected Files:
- `.claude/commands/generate-prp.md`
- `.claude/commands/execute-prp.md`
- `.claude/settings.local.json`

### If You Need to Update Commands:
1. Ask the user explicitly for permission
2. Make changes in a separate branch
3. Test thoroughly before merging
4. Never make changes without explicit user approval

## 🔄 Project Awareness & Context
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASK.md`** before starting a new task. If the task isn't listed, add it with a brief description and today's date.
- **Check `ROADMAP.md`** to understand the current phase and ensure features align with the phase goals.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.
- **When analyzing existing projects** (refactor/retry modes), use Glob and Grep extensively to understand the codebase structure and patterns.

## 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Use clear, consistent imports** (prefer relative imports within packages).
- **Follow PRIMARY_LANGUAGE idioms and best practices**.

## 🧪 Testing & Reliability
- **Always create TEST_FRAMEWORK tests for new features** (functions, classes, routes, etc).
- **After updating any logic**, check whether existing tests need to be updated. If so, do it.
- **Tests should live in a `/tests` folder** mirroring the main app structure.
  - Include at least:
    - 1 test for expected use
    - 1 edge case
    - 1 failure case

## ✅ Task Completion
- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a "Discovered During Work" section.

## 📎 Style & Conventions
- **Use PRIMARY_LANGUAGE** as the primary language.
- **Follow language-specific style guides** and use appropriate linters.
- **Use type hints/annotations** where applicable.
- Write **clear documentation** for every public function/method.
- **Refer to examples/** folder for specific code patterns and conventions.

## 📚 Documentation & Explainability
- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline comment** explaining the why, not just the what.

## 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.

## 📁 Important Files Reference
- **`PLANNING.md`** - Architecture decisions and patterns
- **`TASK.md`** - Current and completed tasks
- **`examples/`** - Code patterns to follow
- **`tests/`** - Test structure examples

## ⚠️ Important Instructions
- Do what has been asked; nothing more, nothing less.
- NEVER create files unless they're absolutely necessary for achieving your goal.
- ALWAYS prefer editing an existing file to creating a new one.
- NEVER proactively create documentation files (*.md) or README files unless explicitly requested.