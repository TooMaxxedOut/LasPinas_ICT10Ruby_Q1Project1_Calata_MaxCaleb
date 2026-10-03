from pyscript import display, document

def generateSKU():
    document.getElementById("sku_output").innerHTML = ""


    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("quantity").value

    if category == "evil"
        display("no.", target="sku_output")
    elif category == "default"
        display("Choose a Product Category first, then click the button after.", target="sku_output")
    else
        sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
        display("SKU: " + sku, target="sku_output")


