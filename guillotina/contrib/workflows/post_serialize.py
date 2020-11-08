from guillotina.interfaces import IResource
from typing import Any
from guillotina.component import query_adapter
from guillotina.contrib.workflows.interfaces import IWorkflowBehavior

def apply_review(context: IResource, result: Any):
    adapter = query_adapter(context, IWorkflowBehavior)
    result['review_state'] = adapter.review_state
