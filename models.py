from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    consent = db.Column(db.Boolean, default=False)
    is_premium = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    membership = db.relationship("Memberships", backref="user")
    plans = db.relationship("WorkoutPlan", backref="user")

class Memberships(db.Model):
    __tablename__ = "memberships"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50))
    is_paid = db.Column(db.Boolean, default=False)
    body = db.Column(db.Text)

class WorkoutPlan(db.Model):
    __tablename__ = "workout_plans"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)