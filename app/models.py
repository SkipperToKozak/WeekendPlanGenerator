from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime


db_url = "sqlite:///database.db"  # Użyj lokalnej bazy danych SQLite do testów


engine = create_engine(db_url)

# Podstawowy obiekt bazowy
Base = declarative_base()
# Definicja modelu dla aktywności (Activity)
class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)        # Nazwa aktywności
    description = Column(Text)                # Opis aktywności
    category = Column(String)                 # Kategoria (np. 'aktywny', 'relaks')
    duration = Column(String)                 # Czas trwania (np. 'krótkie', 'całodniowe')
    mood = Column(String)                     # Poziom energii (np. 'chill', 'energetyczny')
    weather = Column(String)                  # Jakie warunki pogodowe wymagane?
    budget = Column(String)                   # Budżet (np. 'niski', 'średni', 'drogi')
    people = Column(String)                   # Liczba osób (np. 'solo', '2 osoby', 'grupa')
    # created_at = Column(DateTime, default=datetime.utcnow)  # Czas dodania aktywności

    # # Relacja z użytkownikami (w przypadku, gdy użytkownicy mogą dodawać aktywności)
    # user_id = Column(Integer, ForeignKey('users.id'))
    # user = relationship("User", back_populates="activities")