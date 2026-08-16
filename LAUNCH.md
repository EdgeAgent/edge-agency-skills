# EDGE | AGENCY Skills: The Capability Layer for Agentic Work

> **Launch note — August 2026**

Most agent projects do not fail because the model cannot write another paragraph. They fail because the system cannot discover the right capability at the right moment.

EDGE | AGENCY Skills is a public index designed to solve that problem. It organizes **5,484 source-linked skills across 30 domains** into a searchable surface for builders working with code, research, browser automation, data, media, DevOps, productivity, and agent-to-agent systems.

## The idea

Treat skills as infrastructure, not as a folder of prompts. A skill is a reusable capability boundary: a defined job, a source definition, and a path for an agent to invoke or compose it into a larger workflow.

That changes the starting question. Instead of asking, “Which framework should I use?” a builder can ask, “What capability is missing from this agent?” The catalog makes that question searchable.

## What is inside

| Capability domain | What builders can discover |
| :--- | :--- |
| Coding Agents & IDEs | Code generation, refactoring, debugging, and repository workflows |
| Web & Frontend Development | UI construction, web tooling, browser surfaces, and testing |
| Git & GitHub | Version control, releases, pull requests, audits, and GitOps |
| Search & Research | Retrieval, synthesis, academic workflows, and knowledge discovery |
| DevOps & Cloud | CI/CD, infrastructure, deployment, observability, and servers |
| AI & LLMs | Model workflows, inference patterns, prompting, and agent runtimes |
| Media & Speech | Image, video, audio, transcription, and voice capabilities |
| Productivity & Operations | Calendar, communication, documents, CRM, and task automation |

## Why it is useful

The catalog is deliberately source-linked. Each entry routes back to its upstream skill definition so a builder can inspect the implementation, understand the intended scope, and decide whether it belongs in a production system. The index is a discovery layer—not a blanket endorsement—and every skill should be reviewed before installation or use in a sensitive workflow.

The repository also includes a daily automated link verification workflow and a GitHub Pages documentation site for faster browsing. Search the complete catalog at **[edgeagent.github.io/edge-agency-skills](https://edgeagent.github.io/edge-agency-skills/)**, or explore the source repository at **[github.com/EdgeAgent/edge-agency-skills](https://github.com/EdgeAgent/edge-agency-skills)**.

## The builder's loop

1. **Name the missing capability.** Identify the job your agent cannot currently perform.
2. **Search the index.** Filter by domain or search across names and descriptions.
3. **Inspect the source.** Open the upstream definition and review its scope, dependencies, and security posture.
4. **Compose deliberately.** Add only the capability that strengthens the workflow; keep permissions narrow.
5. **Contribute back.** Correct links, improve descriptions, and submit mature skills through the repository's contribution process.

## The larger thesis

The next generation of agent systems will be differentiated less by a single prompt and more by the quality of their capability layer: how discoverable, composable, auditable, and maintainable their skills are.

EDGE | AGENCY Skills is an open attempt to make that layer easier to navigate.

**Explore the index. Find the missing capability. Build the next workflow.**

---

## X / Twitter launch thread

**1/12** Most AI agents do not need another generic prompt. They need the missing capability.

Today we’re launching **EDGE | AGENCY Skills**: a public, searchable index of **5,484 source-linked agent skills across 30 domains**.

Explore: https://edgeagent.github.io/edge-agency-skills/

**2/12** Think of it as a capability layer for agentic work.

Search by the job you need done: code, research, GitHub, browser automation, data, DevOps, media, productivity, and more.

**3/12** The key idea: skills should be discoverable and composable—not buried in scattered repos, prompt snippets, or framework-specific examples.

**4/12** Every catalog entry links back to its upstream definition.

That means you can inspect the source, understand the scope, and make an informed decision before adding a capability to an agent.

**5/12** The library spans 30 capability domains, including:

• Coding Agents & IDEs
• Web & Frontend Development
• Git & GitHub
• Search & Research
• DevOps & Cloud
• AI & LLMs
• Media, speech, and automation

**6/12** The workflow is simple:

Name the missing capability → search the index → inspect the source → compose deliberately → contribute improvements.

**7/12** We built the browsing experience for fast scanning, with domain filters, keyboard search, progressive loading, and direct source links.

Press `/` to search when you open the docs site.

**8/12** The repository is also becoming operational infrastructure.

A scheduled GitHub Action checks the catalog links daily, so broken source paths can be surfaced instead of silently aging inside a README.

**9/12** The library is a discovery layer, not a blanket endorsement.

Review permissions, dependencies, provenance, and security before using any skill in a production or high-consequence workflow.

**10/12** The bigger thesis: the next generation of agents will be differentiated by their capability layer—how well skills are discovered, composed, audited, and maintained.

**11/12** If you build agents, automations, copilots, or multi-agent systems, this is a place to start when your system hits a capability boundary.

**12/12** Explore the index, star the repository, and help improve it:

Docs: https://edgeagent.github.io/edge-agency-skills/
Repo: https://github.com/EdgeAgent/edge-agency-skills

Find the missing capability. Build the next workflow.
