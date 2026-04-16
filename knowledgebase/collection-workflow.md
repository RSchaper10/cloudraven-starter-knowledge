# Collection Workflow

This repo now includes a runnable, no-install collection workflow.

Core files:

- `knowledgebase/manifests/collection-targets.json`
- `knowledgebase/manifests/url-manifest.json`
- `knowledgebase/manifests/url-manifest.md`
- `scripts/collect_docs.py`
- `scripts/build_search_index.py`
- `scripts/search_knowledge.py`

Collection flow:

1. Define the official doc targets and URL guardrails in the collection targets manifest.
2. Run the collector to fetch HTML pages or plain-text doc exports and copy the text into the local store.
3. Persist both extracted page copies and CloudRaven-focused enrichment pages.
4. Build the local search index.
5. Query the index locally.

AWS framework guardrail:

- The AWS target only allows URLs under `https://docs.amplify.aws/nextjs/`.
- This intentionally blocks near-match React or JavaScript docs that can look similar but are out of scope for this repo.

Local store layout:

- `knowledgebase/store/raw_html/<target>/`
- `knowledgebase/store/extracted/<target>/`
- `knowledgebase/store/enriched/<target>/`
- `knowledgebase/index/knowledge.db`
- `knowledgebase/index/tfidf-index.json`

Commands:

```bash
python3 scripts/collect_docs.py
python3 scripts/build_search_index.py
python3 scripts/search_knowledge.py "amplify nextjs auth storage"
```

Collection outputs:

- a visited URL manifest
- copied page text in markdown form
- CloudRaven-focused enrichment notes per collected page
- a local search index for retrieval

Current search model:

- SQLite FTS5 for fast lexical retrieval
- TF-IDF chunk similarity for a local no-install semantic-like ranking layer

Constraint note:

- This is not a true embeddings database like Chroma yet.
- It is the strongest zero-install local option available in the repo right now.
- If you later want Chroma or another vector store, this file layout is ready for an adapter upgrade.
