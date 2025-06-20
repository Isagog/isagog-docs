"""
app/api/endpoints/analysis.py

Defines FastAPI endpoints for document analysis operations.
These endpoints interact with the analysis service.
"""

from fastapi import APIRouter, Request, Depends
from uuid import UUID
from pymongo.collection import Collection

from isagog_docs.schemas.analysis import AnalysisCommit
from isagog_docs.schemas.document import Document
from isagog_docs.services.analysis import AnalysisService

router = APIRouter(prefix="/documents/{document_id}/analysis")

# Singleton service instance
_analysis_service = None

def get_analysis_service(request: Request) -> AnalysisService:
    """Get singleton instance of DocumentAnalysisService."""
    return request.app.state.analysis_service

@router.post("/", status_code=201, response_model=Document, tags=["Analysis"])
async def start_analysis(document_id: UUID, service = Depends(get_analysis_service)):
    """
    **Start analysis for a document.**

    Initiates an asynchronous analysis process for the specified document.
    Returns the initial status of the analysis.
    """
    return await service.start_analysis(document_id)

@router.get("/", response_model=Document, tags=["Analysis"])
async def get_analysis(document_id: UUID, service = Depends(get_analysis_service)):
    """
    **Get analysis for a document for user review.**

    Retrieves the current status and results of the analysis for a document.
    """
    return await service.get_analysis(document_id)

@router.put("/", response_model=Document, tags=["Analysis"])
async def commit_analysis(document_id: UUID, commit_data: AnalysisCommit, service = Depends(get_analysis_service)):
    """
    **Commit analysis for a document.**

    Allows a user to commit (e.g., approve or reject) the results of a document analysis.
    """
    return await service.commit_analysis(document_id, commit_data)
