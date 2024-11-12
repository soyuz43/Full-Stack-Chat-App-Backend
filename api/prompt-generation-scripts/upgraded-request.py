import json

def create_upgraded_query(original_query):
    upgraded_query = {
        "query_id": "LLaMA3_Command_Guide",
        "original_query": original_query,
        "deconstructed_query": {
            "intent": "informative",
            "entities": ["Meta LLaMA 3", "commands", "guide"],
            "keywords": ["syntax", "examples", "best practices", "command combinations", "prompt optimization", "advanced applications"]
        },
        "upgraded_query": {
            "refined_query": "Provide official SYNTAXDOCS for Meta LLaMA 3, detailing: \
                1. Command syntax and parameters. \
                2. Extensive examples and use cases. \
                3. Best practices for optimal usage. \
                4. Command combinations and chaining. \
                5. Prompt engineering and optimization. \
                6. Advanced applications (meta-programming, self-modifying code, recursive nesting). \
                7. Troubleshooting and common issues. \
                8. Real-world applications and case studies. \
                9. Community resources and support.",
            "clarified_intentions": [
                "obtain official documentation",
                "master LLaMA 3 command syntax",
                "exploit optimal usage techniques",
                "unlock advanced capabilities",
                "facilitate practical applications"
            ],
            "suggested_improvements": [
                "include visual diagrams",
                "provide step-by-step tutorials",
                "offer additional resources",
                "document release notes"
            ]
        }
    }
    return upgraded_query


original_query = "Compile an exhaustive, expert-level guide to Meta LLaMA 3 commands, encompassing comprehensive syntax explanations, numerous examples, and best practices for optimal usage, including command combinations, prompt optimization, and advanced applications"


upgraded_query = create_upgraded_query(original_query)


print(json.dumps(upgraded_query, indent=4))