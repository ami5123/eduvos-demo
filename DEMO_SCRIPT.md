# Demo Script: Kiro IDE → GitHub → AWS CodeSuite
## Eduvos Developer Tools Demo

---

## SETUP (Before the demo)
- [ ] Code pushed to GitHub (`ami5123/eduvos-demo`)
- [ ] CodePipeline ran successfully at least once
- [ ] Kiro IDE open with the project loaded
- [ ] Kiro Autonomous Agent connected to the repo
- [ ] Browser tabs open:
  - GitHub repo: https://github.com/ami5123/eduvos-demo
  - CodePipeline: https://eu-west-1.console.aws.amazon.com/codesuite/codepipeline/pipelines/eduvos-demo-pipeline/view
  - CodeBuild: https://eu-west-1.console.aws.amazon.com/codesuite/codebuild/projects/eduvos-demo-build/build-history
  - Kiro Agent: https://app.kiro.dev/agent
- [ ] GitHub issue pre-created: "Add search endpoint to find students by name"

---

## ACT 1: Set the Scene (2 min)

**SAY:**
> "Today I'm going to show you a complete modern developer workflow — from writing code with AI assistance, to automated testing and deployment. This is the same toolchain used by companies shipping software every day."

**SHOW:** The README in GitHub — explain the Student Registration API
> "We have a simple API that Eduvos could use for student registration. Let's walk through how a developer would add a new feature using Kiro and AWS."

---

## ACT 2: Kiro IDE — Writing Code with AI (8 min)

### 2a: Show the project

**DO:** Open `app.py` in Kiro IDE
**SAY:**
> "This is Kiro — an AI-powered IDE built by AWS. Let me show you what makes it different."

**DO:** Highlight the existing endpoints
> "We have a basic student API. Let's say we need to add a new feature — the ability to search students by course."

### 2b: Spec-driven development

**DO:** Open Kiro chat and type:
```
Add a GET endpoint /students/search that accepts a query parameter "course" 
and returns all students enrolled in that course. Include input validation.
```

**SAY:**
> "Watch what happens — Kiro doesn't just write code. It first creates a specification, breaks it into tasks, then implements."

**PAUSE:** Let the audience see the spec and task breakdown.

### 2c: Show the generated code

**DO:** Review the code Kiro generates
**SAY:**
> "Notice it added the endpoint, input validation, AND it follows the same patterns as our existing code. This is spec-driven development — structured, not random."

### 2d: Run tests

**DO:** Open terminal in Kiro, run:
```bash
python3 -m pytest -v
```

**SAY:**
> "All tests pass, including any new ones Kiro generated. Now let's push this to GitHub and watch the CI/CD pipeline take over."

---

## ACT 3: GitHub — Source Control (3 min)

**DO:** In Kiro terminal:
```bash
git add .
git commit -m "feat: add student search by course endpoint"
git push origin main
```

**SAY:**
> "We've pushed our code. Now watch — this automatically triggers our AWS CI/CD pipeline."

**DO:** Switch to browser → GitHub repo → show the new commit

---

## ACT 4: AWS CodePipeline — Automated CI/CD (5 min)

### 4a: Pipeline overview

**DO:** Switch to CodePipeline console
**SAY:**
> "This is AWS CodePipeline. It orchestrates our entire build and test process. You can see two stages — Source and Build."

**DO:** Point to the Source stage turning green
> "Source stage picked up our commit from GitHub automatically."

### 4b: CodeBuild in action

**DO:** Click into the Build stage → click "Details" to show CodeBuild logs
**SAY:**
> "CodeBuild is now installing dependencies and running our test suite. This happens every single time code is pushed — no human intervention needed."

**DO:** Show the pytest output in the build logs
> "All 6 tests passed. In a production setup, this would then deploy automatically. Every student's code gets the same rigorous automated testing."

### 4c: Pipeline success

**DO:** Show the pipeline fully green
**SAY:**
> "Source to Build — all green. The developer pushed code, and within minutes it's been automatically tested. This is CI/CD."

---

## ACT 5: Kiro Autonomous Agent — AI + CI/CD Together (7 min)

**SAY:**
> "Now let me show you something powerful. What if AI could do the entire cycle — write code, open a pull request, and trigger the pipeline — without a developer touching the keyboard?"

### 5a: Assign a task

**DO:** Switch to GitHub → open the pre-created issue "Add search endpoint to find students by name"
**DO:** Add the `kiro` label to the issue

**SAY:**
> "I just assigned this issue to Kiro's autonomous agent. Watch what happens."

### 5b: Show the agent working

**DO:** Switch to https://app.kiro.dev/agent
**SAY:**
> "The agent is now analyzing our codebase, creating a plan, and implementing the feature — all on its own."

**PAUSE:** Let it work for a minute. Show the plan it creates.

### 5c: Show the PR

**DO:** Switch to GitHub → show the PR the agent opened
**SAY:**
> "The agent created a branch, implemented the feature, wrote tests, and opened this pull request — with a detailed description of what it did and why."

**DO:** Show the PR description and code changes

### 5d: Pipeline triggers on PR

**DO:** Show the pipeline/GitHub Actions running on the PR
**SAY:**
> "And look — our CI/CD pipeline automatically runs on this pull request too. The AI writes the code, the pipeline validates it, and a human reviews and approves. That's the complete loop."

---

## ACT 6: Why This Matters for Eduvos (3 min)

**SAY:**
> "Let me bring this back to what this means for your students and institution."

**Key points to hit:**

1. **Industry readiness**
   > "Your graduates will know the same tools used at startups and enterprises — Git, CI/CD, AI-assisted development."

2. **Quality by default**
   > "Every code change is automatically tested. Students learn that shipping code means shipping tested code."

3. **AI as a learning tool**
   > "Kiro doesn't replace the developer — it teaches. Students see how specs are written, how code should be structured, how tests should work."

4. **Scale**
   > "Instructors can use the autonomous agent to generate starter code, review student work, or create example implementations."

5. **Cost**
   > "Kiro has a students program. AWS has education credits. The barrier to entry is low."

---

## CLOSING

**SAY:**
> "What you saw today: AI writes code in Kiro → pushes to GitHub → AWS CodePipeline automatically tests it → humans review and approve. This is modern software development, and your students can start using it today."

**OFFER:**
> "I can help you set this up for a pilot class. Happy to walk through next steps."

---

## BACKUP PLANS

| If this goes wrong... | Do this instead... |
|----------------------|-------------------|
| Pipeline takes too long | Show a pre-recorded run or previous build logs |
| Kiro Agent is slow | Show a pre-made PR you created earlier |
| GitHub push fails | Show the code locally and explain the flow with diagrams |
| CodeBuild fails | Show the buildspec.yml and explain what it does |

---

## TIMING

| Section | Duration |
|---------|----------|
| Set the scene | 2 min |
| Kiro IDE | 8 min |
| GitHub | 3 min |
| CodePipeline + CodeBuild | 5 min |
| Kiro Autonomous Agent | 7 min |
| Why it matters | 3 min |
| **Total** | **~28 min** |
| Q&A buffer | 10-15 min |
