import logging 
from workflow_loader import openJSON


def main():
    workflow = openJSON()

    if workflow is None:
        print("Cannot continue — workflow failed to load.")
        return

    # At this point, workflow is valid JSON
    print("Workflow loaded successfully.")


    # Later:
    # run_workflow(workflow)

if __name__ == "__main__":
    main()


