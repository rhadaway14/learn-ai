# Capstone Threat Model

## Assets

List private data, credentials, model access, tool authority, workflow state, evaluation data, logs, and intellectual property.

## Trust boundaries

Treat user text, uploaded files, retrieved documents, webpages, model output, tool output, MCP servers, and third-party models as untrusted unless independently established otherwise.

## Required threats

- direct and indirect prompt injection;
- cross-tenant retrieval;
- data exfiltration through output or tools;
- excessive agency and confused deputy behavior;
- poisoned sources and dependency supply chain;
- denial of wallet or unbounded execution;
- insecure output rendering;
- secret exposure in prompts, traces, and logs;
- evaluation manipulation.

## Control hierarchy

Prefer isolation, least privilege, authorization, provenance, deterministic validation, human approval, quotas, monitoring, and revocation over asking the model to behave.
