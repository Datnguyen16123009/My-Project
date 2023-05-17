import { Injectable } from '@angular/core';
import { Product } from './product-list/product-list.component';

@Injectable({
  providedIn: 'root',
})
export class PayService {
  productList: Product[] = [];
  constructor() {}
  addProduct(product: Product, soLuong: number) {
    for (let i = 0; i < this.productList.length; i++) {
      if (product.name == this.productList[i].name) {
        this.productList[i]['soLuong'] += soLuong;
        product.tong = product.soLuong * product.price;
        return;
      }
    }
    product.soLuong += soLuong;
    product.tong = product.soLuong * product.price;
    this.productList.push(product);
  }
  getProducts(): Product[] {
    return this.productList;
  }
  delProducts(): Product[] {
    return (this.productList = []);
  }
}
