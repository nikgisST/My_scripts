# Arcpy module is for working with spatial data
import arcpy

# First set the workspace where the data will be stored
arcpy.env.workspace = r"D:\UN\set_DB\databases\GISRO_PILOT.gdb"


# This function will create a square polygon based on a center point and size
def square_polygon(center_x, center_y, size):
    middle_point = size / 2
    vertices = [
              arcpy.Point(center_x - middle_point, center_y - middle_point),
              arcpy.Point(center_x + middle_point, center_y - middle_point),
              arcpy.Point(center_x + middle_point, center_y + middle_point),
              arcpy.Point(center_x - middle_point, center_y + middle_point),
              arcpy.Point(center_x - middle_point, center_y - middle_point)  # Closing the polygon
              ]
    return arcpy.Polygon(arcpy.Array(vertices))


# A dictionary of station values: {OBJECTID: [Geometry Type, Name, X_coordinate, Y_coordinate]}
stations = {
    1: ["Point", "PTCZ 9 GAVANA", -0.910843, 0.338404],
    2: ["Point", "PTCZ 11 GAVANA", -0.594578, 0.37003],
    3: ["Point", "PTCZ 14 GAVANA", 0.082229, -0.290964],
    4: ["Point", "PTCZ 3 GAVANA", -1.068976, -0.433283],
    5: ["Point", "PTCZ 3 GAVANA", 0.638855, 0.550301],
    6: ["Point", "PTCZ 14 GAVANA", -1.606627, 0.7875],
    7: ["Point", "PTCZ 14 GAVANA", 1.530723, -0.815964],
}

# Local variables for creating a new feature class Station_polygon (or shapefile + .shp)
output_path = r"D:\UN\set_DB\databases\GISRO_PILOT.gdb"
output_name = "Station_polygon"
geometry_type = "POLYGON"
template = None
has_m = "DISABLED"
has_z = "DISABLED"
spatial_reference = arcpy.Describe(r"D:\UN\set_DB\databases\GISRO_PILOT.gdb\StationBoundary").spatialReference  #get from existing fc

arcpy.management.CreateFeatureclass(output_path, output_name, geometry_type, template, has_m, has_z, spatial_reference)
output_feature_class = r"D:\UN\set_DB\databases\GISRO_PILOT.gdb\Station_polygon.shp"

# InsertCursor adds square polygons to the new feature class
with arcpy.da.InsertCursor(output_feature_class, ["SHAPE@"]) as cursor:
    for OBJECTID, station_values in stations.items():
        SIZE_SQUARE = 1
        station_name = station_values[1]
        center_x = station_values[2]
        center_y = station_values[3]
        polygon = square_polygon(center_x, center_y, SIZE_SQUARE)  # Create a square polygon
        cursor.insertRow([polygon])  # Insert the polygon into the feature class

print("Successful")
