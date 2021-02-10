# JSON LD Contexts
This directory contains a variety of contexts for use with the JSON-LD module

## JSON LD 1.0 contexts
### context directory
* [termci_schema.context.jsonld]() - default context emitted by the current version (as of writing 1.7.0) of biolinkml

### frame directory  
* [termci_schema.frame.jsonld]() - default context with framing information added

## JSON LD 1.1 contexts
### context directory
* [Package.context.jsonld]() - Package context (hand generated)
* [ConceptSystem.context.jsonld]() - ConceptSystem context (hand generated)
* [ConceptReference.context.jsonld]() - ConceptReference context (hand generated)
* [termci_namespaces.context.jsonld]() - experimental module for separate namespaces, including explicit namespace
  identifier for namespaces that end with a '_' (hand generated)
* [termci_schema_inlined.context.jsonld]() - Nested contexts inlined (generated using context_flattener.py starting
  with Package.context.jsonld)
  
### frame directory
* [termci_schema.frame.jsonld]() - frame that links directly to Package
* [termci_schema_inlined.frame.jsonld]() - framed schemas with nested context inlined

## Starting the docker web server
```bash
> cd jsonld-context
> docker image build . -t context_server
> docker run -it --rm -d -p <port>:80 --name context_server -v `pwd`:/usr/share/nginx/html context_server
``

## TODO
1) Determine whether the separate namespace module should be included as a full-fledged context or as an `@import`
2) Investigate the use of framing 