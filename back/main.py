from fastapi import HTTPException

from .app.models import Phrase
from .app.pydantics import PhrasePydantic, PhraseUpdatePydantic
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
    return {"message": m_phrase.message}


@app.post("/create-phrase")
def create_phrase(phrase: PhrasePydantic):
    if Phrase.objects(key=phrase.key).first() is not None:
        raise HTTPException(status_code=400, detail="The phrase already exists.")

    m_phrase = Phrase(key=phrase.key, tags=phrase.tags)
    m_phrase.set_message(phrase.message)
    m_phrase.save()
    return {'message': f'Phrase with key {phrase.key} created.'}


@app.put("/update-phrase/{phrase_id}")
def update_phrase(phrase_id: str, phrase: PhraseUpdatePydantic):
    m_phrase = Phrase.objects(id=phrase_id).first()
    if m_phrase is None:
        raise HTTPException(status_code=404, detail="This phrase doesn't exists.")

    if phrase.key is not None:
        m_phrase.key = phrase.key
    if phrase.message is not None:
        m_phrase.set_message(phrase.message)
    if phrase.tags is not None:
        m_phrase.tags = phrase.tags
    m_phrase.save()
    return {'message': f'Phrase with key {phrase.key} updated.'}


@app.delete("/remove-phrase/{phrase_id}")
def remove_phrase(phrase_id: str):
    m_phrase = Phrase.objects(id=phrase_id).first()
    if m_phrase is None:
        raise HTTPException(status_code=404, detail="This phrase doesn't exists.")

    m_phrase.delete()
    return {'message': f'Phrase with key {m_phrase.key} deleted.'}
