from pydantic import BaseModel          #Pydantic = validation + serialization engine.
                                        #FastAPI depends heavily on it.
class PromptRequest(BaseModel):
    prompt: str                         #Request body MUST contain string prompt.

class PromptResponse(BaseModel):
    success: bool
    output: str


"""FastAPI automatically:
- validates
- parses JSON
- generates docs"""