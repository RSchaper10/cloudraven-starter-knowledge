.PHONY: kb-sync kb-index kb-collect kb-search

kb-sync:
	python3 scripts/sync_knowledge.py

kb-index:
	python3 scripts/build_search_index.py

kb-collect:
	python3 scripts/collect_docs.py $(if $(targets),--targets $(targets),)

kb-search:
	python3 scripts/search_knowledge.py "$(q)" $(if $(top),--top-k $(top),)
