# delphy / memo
## Knowledge Base for your GPT

# Vision
Delphy is a unified knowledge base for your GPT, ChatGPT or Copilot.
You can connect to your favorite applications and unlock information stored within.

#### Open-Source
- Transparency how your data is processed and stored

#### Extensible
- Write your own connector

#### Integrations
- Integrations into your favourite Chat application (ChatGPT, MS Copilot, ...)
- Accesible from anywhere (Apps, Web, Browser Plugin, ...)

# Concept
- Connectors: Connect your datasources and apps. Sync or search them.
- Synchronizer: Incrementaly syncs your connections to the datastore
- Datastores: Compatible with multiple VectorDBs
- Retriever: Retrieves the right pieces of information for your query and context
- Integrations: APIs for integrations (ChatGPT, General API, ...)
- Services: File parsing, chunking and embedding as service for Connectors
- Frontend: UI for settings

# Roadmap
Connectors:
- [] Local Files
- [] Notion
- [] Browser

Integrations:
- [] API
- [] ChatGPT Plugin

Databases:
- [] chromadb
- [] Weaviate

Ideas:
- Executable package
- Smart sync: Decide which files to sync
- Search: Search in connectors
- Multiuser
- Hosted App (Authentication, Database, Limits, Payment)
- Queue: Side processing of heavy compute loads (file parsing, embeddings)
- Spaces: Group connectors in spaces. Select to which spaces integrations have access.
- More Integrations: Apps, Browser Plugins, Third Party Apps
