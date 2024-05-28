from Trapezoid import Trapezoid


class IsoscelesTrapezoid(Trapezoid):
    def calculate_angles(self):
        base_angle = super().calculate_angles()[0]
        return (base_angle, base_angle, 180 - base_angle, 180 - base_angle)
