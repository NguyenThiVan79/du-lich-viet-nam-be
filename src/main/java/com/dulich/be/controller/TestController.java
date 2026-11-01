package com.dulich.be.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {

    // @GetMapping("/api/test")
    // public String test() {
    //     return "Backend Du Lich Viet Nam dang hoat dong!";
    // }
    @GetMapping("/api/hello")
    public String hello() {
        return "Xin chào";
    }
}