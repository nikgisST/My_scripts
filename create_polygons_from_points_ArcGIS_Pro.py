# Import the arcpy module for working with spatial data
import arcpy

# Set the workspace where the data will be stored
arcpy.env.workspace = r"C:\EsriTraining\mim"


# Define a function to create a square polygon based on a center point and size
def square_polygon(x, y, size):
    middle_point = size / 2
    vertices = [
              arcpy.Point(center_x - middle_point, center_y - middle_point),
              arcpy.Point(center_x + middle_point, center_y - middle_point),
              arcpy.Point(center_x + middle_point, center_y + middle_point),
              arcpy.Point(center_x - middle_point, center_y + middle_point)
    ]
    return arcpy.Polygon(arcpy.Array(vertices))


# Define a dictionary of stations with their attributes
stations = {
    1: ["Point", "niki", -0.910843, 0.338404],
    2: ["Point", "stefi", -0.594578, 0.37003],
    3: ["Point", "ani", 0.082229, -0.290964],
    4: ["Point", "mimi", -1.068976, -0.433283],
    5: ["Point", "mimi", 0.638855, 0.550301],
    6: ["Point", "ani", -1.606627, 0.7875],
    7: ["Point", "ani", 1.530723, -0.815964],
}

# Set local variables for creating a new feature class (shapefile)
out_path = r"C:\EsriTraining\mim"
out_name = "polygon.shp"
geometry_type = "POLYGON"
template = None
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_ref = arcpy.Describe(r"C:\EsriTraining\mim\Polygon_ani_6.shp").spatialReference

# Create a new feature class
arcpy.management.CreateFeatureclass(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)

# Set the output feature class path
output_fc = r"C:\EsriTraining\mim\Polygon.shp"

# Use an InsertCursor to add square polygons to the new feature class
with arcpy.da.InsertCursor(output_fc, ["SHAPE@"]) as cursor:

    for each_station_id, station_values in stations.items():
        station_name = station_values[1]
        center_x = station_values[2]
        center_y = station_values[3]

        # Set the size of the square polygon
        size_polygon = 1

        # Create a square polygon
        polygon = square_polygon(center_x, center_y, size_polygon)

        # Insert the polygon into the feature class
        cursor.insertRow([polygon])

print("Successful")
