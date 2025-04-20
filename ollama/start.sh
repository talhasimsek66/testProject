#!/bin/sh
export model=gemma3:1b
export OLLAMA_HOST=0.0.0.0:11434
ollama start &
ollama run $model
