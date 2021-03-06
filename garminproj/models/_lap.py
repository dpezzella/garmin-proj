from sqlalchemy import Column, Interval, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from ._base import Base
from ._track_point import TrackPoint


class Lap(Base):
    __tablename__ = 'laps'

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activities.id'))
    lap_number = Column(Integer)
    start_time = Column(Interval)
    lap_seconds = Column(Float)
    lap_meters = Column(Float)
    max_speed = Column(Float)
    calories = Column(Integer)
    avg_hr = Column(Integer)
    max_hr = Column(Integer)
    intensity = Column(String)
    trigger_method = Column(String)

    activity = relationship(
            'Activity', back_populates='laps'
    )

    track_points = relationship(
            'TrackPoint', order_by=TrackPoint.time, back_populates='lap'
    )