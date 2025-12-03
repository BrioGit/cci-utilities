# BRIOLabs | CCI Utilties
This utiliy repo is designed to expose common tasks to other BRIOLabs projects. 

## Usage
To use the tasks in this repo, add a sources section to the top of your cumulusci.yml file. 
```yml
sources:
    brio:
        github: https://github.com/BrioGit/cci-utilities
        allow_remote_code: True
```

You can then call the task in your remote project
```yml
flows:
    dev_org:
        steps:
            0.1:
                task: brio:layout_event_remove_related_content_items
```

## Task Definitions

### Layout Metadata Transform

#### Remove Metadata from the Event Layout
This task removes elements from the layout metdata item.  The task is configured to remove elements with the name "relatedContent" from the Event Layout. 
EG: 
```yml
flows:
    dev_org:
        steps:
            0.1:
                task: brio:layout_event_remove_related_content_items
```
