from stl import mesh

def load_3d_model(model_path):
    model = mesh.Mesh.from_file(model_path)
    return model
