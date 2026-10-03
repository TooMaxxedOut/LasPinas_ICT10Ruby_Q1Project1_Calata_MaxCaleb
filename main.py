from pyscript import display, document

def generateSKU(e):
    document.getElementById("skew_output").innerHTML = ""


    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("quantity").value

    if category == "evil"
    display("no.", target="skew_output")
    elif category == "default"
        display("Choose a Product Category first, then click the button after.", target="skew_output")
    else
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
    display("SKU: " + sku, target="skew_output")


