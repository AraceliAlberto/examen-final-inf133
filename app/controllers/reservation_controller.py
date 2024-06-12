from flask import Blueprint, request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from app.models.reservation_model import Reservations
from app.views.reservation_view import render_reservations_list, render_reservation_detail
from app.utils.decorators import jwt_required, role_required
from datetime import datetime


reservation_bp = Blueprint("reservation", __user_id__)

@reservation_bp.route("/reservations", methods=["GET"])
@jwt_required
def get_reservations():
    reservations = Reservations.get_all()
    return jsonify(render_reservations_list(reservations))

@reservation_bp.route("/reservations/<int:id>", methods=["GET"])
@jwt_required
def get_reservation(id):
    reservation = reservation.get_by_id(id)
    if reservation:
        return jsonify(render_reservation_detail(reservation))
    return jsonify({"error": "reservation no encontrado"}), 404

@reservation_bp.route("/reservations", methods=["POST"])
@jwt_required
@role_required(role=["admin"])
def create_reservation():
    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")

    reservation_date = request.form['fecha_Nacimiento']
    fecha = datetime.strptime(fecha, '%Y-%m-%d').date()

    if not user_id or not restaurant_id or not fecha or not num_guests or not special_requests or not status:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    reservation = Reservations(user_id=user_id, restaurant_id=restaurant_id, reservation_date=reservation_date, num_guests=num_guests, special_requests=special_requests, status=status)
    reservation.save()
    return jsonify(render_reservation_detail(reservation)), 201

@reservation_bp.route("/reservations/<int:id>", methods=["PUT"])
@jwt_required
@role_required(role=["admin"])
def update_reservation(id):
    reservation = Reservations.get_by_id(id)

    if not reservation:
        return jsonify({"error": "reservation no encontrado"}), 404

    data = request.json
    
    if "user_id" in data:
        reservation.user_id = data['user_id']
    if "restaurant_id" in data:
        reservation.restaurant_id = data['restaurant_id']
    if "reservation_date" in data:
        reservation.reservation_date = data['reservation_date']
    if "num_guests" in data:
        reservation.num_guests = data['num_guests']
    if "special_requests" in data:
        reservation.special_requests = data['special_requests']
    if "status" in data:
        reservation.status = data['status']

    reservation.save()
    return jsonify(render_reservation_detail(reservation))

@reservation_bp.route("/reservations/<int:id>", methods=["DELETE"])
@jwt_required
@role_required(role=["admin"])
def delete_restaurant(id):
    reservation = Reservations.get_by_id(id)
    if not reservation:
        return jsonify({"error": "reservation no encontrado"}), 404

    reservation.delete()
    return "", 204