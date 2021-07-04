from fastapi import HTTPException

from .app.models import Phrase
from .app.pydantics import PhrasePydantic
from .app.settings import app


@app.get("/")
def read_root():
    phrases = [phrase.as_json() for phrase in Phrase.objects]
    return phrases


@app.get("/{phrase_id}")
def detail_phrase(phrase_id: str):
    m_phrase = Phrase.objects(id=phrase_id).first()
    if m_phrase is None:
        raise HTTPException(status_code=404, detail="This phrase doesn't exists.")
    return m_phrase.as_json(decoded=True)


@app.get("/decode-phrase/{phrase_id}")
def decode_phrase(phrase_id: str):
    m_phrase = Phrase.objects(id=phrase_id).first()
    if m_phrase is None:
        raise HTTPException(status_code=404, detail="This phrase doesn't exists.")
    return {"secrets": m_phrase.secrets}


@app.post("/create-phrase")
def create_phrase(phrase: PhrasePydantic):
    if Phrase.objects(title=phrase.title).first() is not None:
        raise HTTPException(status_code=400, detail="The phrase already exists.")

    m_phrase = Phrase(title=phrase.title)
    m_phrase.set_secrets(phrase.secrets)
    m_phrase.save()
    return {'message': f'Phrase with title {phrase.title} created.'}


@app.put("/update-phrase/{phrase_id}")
def update_phrase(phrase_id: str, phrase: PhrasePydantic):
    m_phrase = Phrase.objects(id=phrase_id).first()
    if m_phrase is None:
        raise HTTPException(status_code=404, detail="This phrase doesn't exists.")

    if phrase.title is not None:
        m_phrase.title = phrase.title
    if phrase.secrets is not None:
        m_phrase.set_secrets(phrase.secrets)
    m_phrase.save()
    return {'message': f'Phrase with title {phrase.title} updated.'}


@app.delete("/remove-phrase/{phrase_id}")
def remove_phrase(phrase_id: str):
    m_phrase = Phrase.objects(id=phrase_id).first()
    if m_phrase is None:
        raise HTTPException(status_code=404, detail="This phrase doesn't exists.")

    m_phrase.delete()
    return {'message': f'Phrase with title {m_phrase.title} deleted.'}
