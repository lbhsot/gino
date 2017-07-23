import pytest
from .models import db

@pytest.fixture(scope='module')
async def pool():
    async with db.create_pool('postgresql://localhost/gino') as pool:
        yield pool
