#!/bin/sh
model=gemma3:1b
export OLLAMA_HOST=0.0.0.0:911
ollama start &
ollama run $model
