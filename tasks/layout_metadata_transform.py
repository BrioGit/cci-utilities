from typing import Optional
from cumulusci.tasks.metadata_etl import MetadataSingleEntityTransformTask
from cumulusci.utils.xml.metadata_tree import MetadataElement
from cumulusci.core.utils import process_bool_arg 



class Remove(MetadataSingleEntityTransformTask):
    ## Subclasses *must* define `entity`
    entity = "Layout"

    ## Most subclasses include the base class's options via
    ## **MetadataSingleEntityTransformTask.task_options. Further
    ## options may be added for this specific task. The base class
    ## options include in particular the standard `api_names` option,
    ## which base class functionality requires.
    task_options = {
        "element_name": {
            "description": "Name of the element to remove",
            "required": True,
        },
        **MetadataSingleEntityTransformTask.task_options,
    }

    ## The `_transform_entity()` method must be overriden.
    def _transform_entity(
        self, metadata: MetadataElement, api_name: str
    ) -> Optional[MetadataElement]:
        ## This method modifies the layoutAssingments element of the profile to assign the provided page layout

        element_name = self.options["element_name"]

        ##Find the layoutAssignments element in the profile metadata
        element = metadata.find(element_name)

        if element is None:
            ## If the related content is not found, then we're done
            print("No element found with name " + element_name + ".")
        else:
            print("Element Found");
            #print(element.tostring());
            metadata.remove(element);
                
        #print(metadata.tostring())
        ## Always return the modified `MetadataElement` if deployment is desired.
        ## To not deploy this element, return `None`.

        
        return metadata