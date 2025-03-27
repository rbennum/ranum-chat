from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/auth')

@router.get('/signup')
async def signup():
	return {'signup': 'success'}

@router.get('/signin')
async def signin():
	return {'signin': 'success'}

@router.get('/logout')
async def logout():
	return {'logout': 'success'}
